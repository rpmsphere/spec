%global debug_package %{nil}

Summary: 	PC Performance Testing
Name: 		performancetest
Version: 	10.2
Release: 	1003.bin
License: 	Commercial, free evaluation
Group:		Hardware/Tools
Source0:	https://www.passmark.com/downloads/pt_linux_x64.zip
URL:		http://www.passmark.com/products/pt_linux/download.php
Requires:	ncurses

%description
Passmark's PerformanceTest for Linux/Mac is a software tool 
that allows everybody to quickly assess the performance
of their computer and compare it to a number
of standard 'baseline' computer systems.

%prep
%setup -q -n PerformanceTest

%build

%install
install -Dm755 pt_linux_x64 %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc readme.txt
%{_bindir}/%{name}

%changelog
* Sun Dec 18 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 10.2
- Initial binary package
