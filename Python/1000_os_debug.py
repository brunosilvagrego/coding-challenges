import os
import sys

# Reset VM
os.system('vmrun -T ws reset /home/ctw00982/testmanager/work/20w34.3-1_MGU_KHMBvx/vm_SINT_JOB_3297/hu/mgu-20w34.3-1-29-dirty-062694-mgu-high-images/vmwx86/mgu-20w34.3-1-29-dirty-062694-image-high-vmwx86_v12.vmx')

# ps -aux | grep vmx
os.system('ps -aux | grep vmx')

print()
print(os.name)
print(os.uname())
print(sys.platform)