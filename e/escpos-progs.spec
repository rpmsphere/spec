%undefine _debugsource_packages

Name:           escpos-progs
Version:        2018
Release:        3.1
Summary:        Misc. ESC/POS Programs
License:        free
Group:          Applications/Utilities
Source0:        png2escpos-master.zip
Source1:        escposf.c
BuildRequires:  libpng-devel

%description
png2escpos <https://github.com/twg/png2escpos>:
Quickly convert PNG files to ESC/POS format, for printing on Epson thermal point-of-sale printers.
escposf <https://kg4zqz.blogspot.tw/2016/08/escposf-thermal-printer-filter-and.html>:
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

%files
%doc LICENSE README.md
%{_bindir}/*

%changelog
* Tue Apr 03 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2018
- Rebuilt for Fedora
