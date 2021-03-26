%global debug_package %{nil}

Name:           coolmail
BuildRequires:  xorg-x11-utils libX11-devel libXt-devel libXext-devel
Version:        1.3
Release:        5.1
License:        GPL v2 or later
Source:         coolmail-1.3.tar.gz
Patch0:	        coolmail-getlogin.patch
Group:          Productivity/Networking/Email/Utilities
Summary:        A mail notification utility with 3D animated graphics

%description
Coolmail watches your inbox and lets you know when you have mail.
Clicking on coolmail can launch your mail reading/writing utility.
While your mail utility is open, clicking on coolmail will cause it
to check your inbox at that instant, without waiting for the next
regular interval.

%prep
%setup
%patch0 -p1

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1 $RPM_BUILD_ROOT/usr/bin
make MANDIR=$RPM_BUILD_ROOT/%_mandir/man1 BINDIR=$RPM_BUILD_ROOT/usr/bin install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/coolmail
%doc README README.changes
%{_mandir}/man1/coolmail.1.gz

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuild for Fedora
* Sat Nov 29 2008 kurt.ziegenbein@web.de
- packaged coolmail version 1.3
