#!/bin/bash
cp /home/ubuntu/projectsknf/sknf.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable sknf
systemctl start sknf # or, service sknf start
