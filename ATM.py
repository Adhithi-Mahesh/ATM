from decimal import Decimal
import mysql.connector as  m
x=m.connect(database='atm_acc',password='admin@123',user='root',host='localhost')
y=x.cursor()


def login() :
      a=int(input('Enter the Account Number :'))
      b=int(input('Enter the Pin :'))
      q= 'SELECT *from acc_holders where acc_number={} and pin = {} ;'.format(a,b)
      y.execute(q)
      z=y.fetchone()
      if z is None:
           print('The Entered PIN / Account Number is INCORRECT')
           incorrect()
      else:
           print('Which Operation is to be executed ? \n1.Check Balance \n2.Withrawal \n3.Deposit')
           ch= int(input('Enter The Operation to be Executed :'))
           if ch == 1:
                balance(a,b)
           elif ch==2 :
                withdrawal(a,b)
           elif ch== 3 :
               deposit(a,b)
           else :
                 print('Invalid Choice')
                 incorrect()


def balance(a,b):
     q= 'SELECT acc_number, holder_name,balance from acc_holders where acc_number={} and pin = {};'.format(a,b)
     y.execute(q)
     z=y.fetchone()
     print('Account Number :',z[0],'\nHolder Name:',z[1], '\nBalance:',z[2])
     logout()
     
def withdrawal(a,b):
      c=int(input('Enter the Amount to be Withdrawn :'))
      q= 'SELECT acc_number, holder_name,balance from acc_holders where acc_number={} and pin = {};'.format(a,b)
      y.execute(q)
      z=y.fetchone()
      if Decimal(z[2]) < Decimal(c) :
          print('Insufficient Balance')
          insufficient(a,b)
          return
      l = str(Decimal(z[2]) - Decimal(c))  
      q1 = "UPDATE acc_holders SET balance={} WHERE acc_number={} AND pin='{}'".format(l, a, b)
      y.execute(q1)
      x.commit()
      q = "SELECT acc_number, holder_name, balance FROM acc_holders WHERE acc_number={} AND pin='{}'".format(a, b)
      y.execute(q)
      z = y.fetchone()
      print('Account Number :',z[0],'\nHolder Name:',z[1], '\nBalance:',z[2])
      logout()

def deposit(a,b):
      c=int(input('Enter the Amount to be Deposited :'))
      q= 'SELECT acc_number, holder_name,balance from acc_holders where acc_number={} and pin = {};'.format(a,b)
      y.execute(q)
      z=y.fetchone()
      l = str(Decimal(z[2]) + Decimal(c))  
      q1 = "UPDATE acc_holders SET balance={} WHERE acc_number={} AND pin='{}'".format(l, a, b)
      y.execute(q1)
      x.commit()
      q = "SELECT acc_number, holder_name, balance FROM acc_holders WHERE acc_number={} AND pin='{}'".format(a, b)
      y.execute(q)
      z = y.fetchone()
      print('Account Number :',z[0],'\nHolder Name:',z[1], '\nBalance:',z[2])
      logout()

def incorrect():
     w= input ('Do you want to Restart ? (y/n)' )
     if w in 'Yy' :
          login()
     else :
          print(' Thank You !  \n Have A Great Day !!')
          x.close()

def logout():
     ch = input('Do You Want to perform another Operation ? (y/n):')
     if ch in 'Yy':
          login()
     else :
          print(' Thank You ! \n Have A Great Day !!')
          x.close()
          
def insufficient(a,b):
      t= input('Do You Want to Re-Enter The Amount ? (y/n) ')
      if t in 'Yy':
         withdrawl(a,b)
      else :
           logout()
      return
login()

