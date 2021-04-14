Name: tomb
Summary: The Crypto Undertaker
Version: 2.9
Release: 1
Group: Applications/Archiving
License: GPLv3
URL: http://www.dyne.org/software/tomb/
Source0: https://files.dyne.org/.xsend.php?file=tomb/Tomb-%{version}.tar.gz
BuildArch: noarch
Requires: zsh

%description
Tomb aims to be a free and open source system for easy encryption and
backup of personal files, written in code that is easy to review and
links shared GNU/Linux components.

At present time, Tomb consists of a simple shell script (Zsh) using
standard filesystem tools (GNU) and the cryptographic API of the Linux
kernel (cryptsetup and LUKS). Tomb can also produce machine parsable
output to facilitate its use inside graphical applications.

%prep
%setup -q -n Tomb-%{version}

%build

%install
%make_install PREFIX=/usr
%make_install PREFIX=/usr -C extras/translations

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_mandir}/man?/%{name}.?.*

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.9
- Rebuilt for Fedora
