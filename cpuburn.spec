%define debug_package	%nil

Summary:	CPU testing utilities
Name:		cpuburn
Version:	1.4a
Release:	6
License:	GPLv2+
Group:		Monitoring
URL:		http://pages.sbcglobal.net/redelm/
Source0:	%{name}-%{version}.tar.gz

%description
CPU testing utilities in optimized assembler for maximum loading P6 (Intel
Pentium Pro, Pentium II, Celeron and Pentium III TM), AMD K6, and P5
Pentium chips.

%files
%doc Design README
%{_bindir}/*

%prep
%setup -q

%build
gcc -m32 -s -nostdlib -o burnP6 burnP6.S
gcc -m32 -s -nostdlib -o burnBX burnBX.S
gcc -m32 -s -nostdlib -o burnK6 burnK6.S
gcc -m32 -s -nostdlib -o burnK7 burnK7.S
gcc -m32 -s -nostdlib -o burnMMX burnMMX.S
gcc -m32 -s -nostdlib -o burnP5 burnP5.S

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 {burnP6,burnBX,burnK6,burnK7,burnMMX,burnP5} \
	%{buildroot}%{_bindir}

%changelog
* Wed Feb 14 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4a
- Rebuild for Fedora
* Wed Dec 13 2017 st <sergei.a.trusov@ya.ru> 1.4a-6
- (563aad1) Merge pull request #1 from st/cpuburn:rosa2016.1
- (563aad1) Added a package for x64 (with 32bit binaries)
