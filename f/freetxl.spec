%undefine _debugsource_packages

Summary: Free TXL Language
Name: freetxl
Version: 10.8b
Release: 1.bin
License: Free Software
Group: Applications
URL: http://www.txl.ca/
Source0: 15528-txl10.8b.linux64.tar.gz
ExclusiveArch: x86_64

%description
FreeTxl is provided by the Txl Project of the Source Transformation Laboratory
at Queen's University. Designed to be free for any use and freely distributable
to all platforms, FreeTxl is an XML -based Txl compiler/interpreter that can
handle any kind of transformation task, no matter how big or complex.

%prep
%setup -q -n txl10.8b.linux64

%build
#No build

%install
install -d %{buildroot}%{_bindir}
install -m755 bin/* %{buildroot}%{_bindir}
sed -i 's|/usr/local/lib|/usr/lib64|' %{buildroot}%{_bindir}/txlc %{buildroot}%{_bindir}/txlp
install -d %{buildroot}%{_libdir}/txl
cp lib/* %{buildroot}%{_libdir}/txl
install -d %{buildroot}%{_mandir}/man1
install -m644 man/man1/* %{buildroot}%{_mandir}/man1

%files
%doc *.txt *.html
%{_bindir}/txl*
%{_libdir}/*
%{_mandir}/man?/*

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 10.8b
- Rebuilt for Fedora
