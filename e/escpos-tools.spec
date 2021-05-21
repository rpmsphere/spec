Name:		escpos-tools
Version:	2018
Release:	1
Summary:	Misc. ESC/POS Tools
License:	free
Group:		Applications/Utilities
Source0:	png2escpos-master.zip
Source1:	escposf.c

%description
png2escpos <https://github.com/twg/png2escpos>:
Quickly convert PNG files to ESC/POS format, for printing on Epson thermal point-of-sale printers.
escposf <http://kg4zqz.blogspot.tw/2016/08/escposf-thermal-printer-filter-and.html>:
A Thermal Printer Filter and Control Command for Linux.

%prep
%setup -q -n png2escpos-master

%build
cc -O3 png2escpos.c -lpng -o png2escpos
cc -O3 %{SOURCE1} -o escposf

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m755 png2escpos escposf %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%doc LICENSE README.md
%{_bindir}/*

%changelog
* Tue Apr 03 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2018
- Rebuilt for Fedora
