Summary: X File Manager
Name: xfm
Version: 1.5.4
Release: 2.1
License: freeware
Group: X11/Applications
URL: https://www.musikwissenschaft.uni-mainz.de/~ag/xfm/
Source: %{name}-%{version}.tar.gz
BuildRequires: Xaw3d-devel

%description
xfm is a file manager for X windows that allows you to manipulate files 
and directories in an intuitive, easy-to-understand manner, as well as 
allowing you to extend itself with other programs.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make 

%install
%make_install

%files
%doc COPYING ChangeLog README* TODO
/etc/X11/app-defaults/Xfm
/etc/X11/xfm
%{_bindir}/xfm*
%{_mandir}/man?/xfm*.?.*
%{_datadir}/xfm

%changelog
* Fri Jun 05 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.4
- Rebuilt for Fedora 
* Sun Oct 26 2003 Chip Cuccio <chipster@norlug.org> 1.4.3-1
- initial build for rh-7.3
