import pefile

import pefile
import sys


PEfile_Path = r"D:\softinstall\WinHex\WinHex.exe"
#PEfile_Path = r"G:\msvcp110.dll"
pe = pefile.PE(PEfile_Path)

print(pe)

'''''
pe_file = open('PE.txt', 'w')
console = sys.stdout
sys.stdout = pe_file
#PE全面解析
print pe
sys.stdout = console
pe_file.close()
'''

#入口点
#print hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint)

'''''
#节表
for section in pe.sections:
    print section
#print hex(pe.sections[i].Characteristics)
'''

'''''
#导入表
for importeddll in pe.DIRECTORY_ENTRY_IMPORT:
    print importeddll.dll, ':'
    #print pe.DIRECTORY_ENTRY_IMPORT[0].dll
    for importedapi in importeddll.imports:
        print '\t', hex(importedapi.address), importedapi.name
    #print pe.DIRECTORY_ENTRY_IMPORT[0].imports[0].name
'''

'''''
#从入口点开始反汇编
ep = pe.OPTIONAL_HEADER.AddressOfEntryPoint
ep_ava = ep + pe.OPTIONAL_HEADER.ImageBase
data = pe.get_memory_mapped_image()[ep:ep+200]
offset = 0
while offset < len(data):
  i = pydasm.get_instruction(data[offset:], pydasm.MODE_32)
  #打印不换行，加,
  print hex(ep + offset), '\t',
  print pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, ep_ava+offset)
  offset += i.length
'''

'''''
#导出符号
#例如calc.exe无导出信息则不存在DIRECTORY_ENTRY_EXPORT变量会出错
for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
    print hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal
'''

'''''
#改写PE信息
pe.OPTIONAL_HEADER.AddressOfEntryPoint = 0xdeadbeef
pe.write(filename='file_to_write.exe')
'''