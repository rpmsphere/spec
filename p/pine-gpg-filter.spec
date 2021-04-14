Name:      pine-gpg-filter
Version:   0.72
Release:   5.1
BuildArch: noarch
Summary:   Wrapper scripts for using multiple roles with GnuPG and Pine
License:   GPL
Group:     System/Base
URL:       http://linux-ip.net/sw/pine-gpg-filter/
Source0:   %{name}-%{version}.tar.gz
Requires:  gpg pine
BuildRoot: %{_tmppath}/%{name}-%{version}-root/

%description
The distinguishing characteristic of this package (when compared
against similar pine and gpg wrappers) is its ability to handle
multiple roles or identities (i.e. different keys for different
email addresses). Unlike some of the other pine and gpg wrappers,
this one performs no passphrase caching (consider using gpg-agent
in gnupg2).

%prep
%setup -q

%build

%install
rm -rf "$RPM_BUILD_ROOT"
install -d $RPM_BUILD_ROOT/%{_bindir}
install %{name} $RPM_BUILD_ROOT/%{_bindir}
$RPM_BUILD_ROOT/%{_bindir}/%{name} --build-symlinks

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/*

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.72
- Rebuilt for Fedora

* Tue Sep 11 2007 Lenz Grimmer <lenz@grimmer.com>
Initial package for the openSUSE build service (Version 0.72), based 
on the author's RPM spec file.

* Sun Oct  8 2006 Martin A. Brown <martin@linux-ip.net> 0.72-2
0.72-2 improving build system, so only derived files are stored in VCS

* Sat Sep  9 2006 Martin A. Brown <martin@linux-ip.net> 0.71-1
0.71-1 initial packaging
