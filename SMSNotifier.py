# -*- coding: utf-8 -*-
"""
Created on Tue Apr 08 09:54:34 2014

@author: julian.irwin@gmail.com
"""
import smtplib

class SMSNotifier(object):
  def __init__(self, gmail_usr, gmail_pwd, from_addr, to_addrs):
    self.server = smtplib.SMTP( "smtp.gmail.com", 587 )
    self.tls_response = self.server.starttls()
    self.usr, self.pwd = gmail_usr, gmail_pwd
    self.login_response = self.server.login(self.usr, self.pwd)
    self.from_addr = from_addr
    self.to_addrs = to_addrs

  def send(self, msg):
    try:
      self.server.sendmail(self.from_addr, self.to_addrs, msg)
    except smtplib.SMTPServerDisconnected:
      self.reconnect()
      self.send(msg)

  def check_responses(self):
    print self.tls_response
    print self.login_response

  def reconnect(self):
    self.server = smtplib.SMTP( "smtp.gmail.com", 587 )
    self.tls_response = self.server.starttls()
    self.login_response = self.server.login(self.usr, self.pwd)
