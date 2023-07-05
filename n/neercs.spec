Summary:	Caca screen manager
Name:		neercs
Version:	0.0.4342
Release:	11.1
License:	WTFPL
Group:		Terminals
URL:		https://caca.zoy.org/wiki/neercs
Source0:	%{name}-0.0.tar.bz2
Source1:	neercs.pam
BuildRequires:	pam-devel python2-devel
BuildRequires:	libcaca-devel
BuildRequires:  automake

%description
Like GNU screen, it allows you to detach a session from a terminal,
but provides unique features:
 * Grabbing a process that you forgot to start inside neercs
 * Great screensaver
 * 3D rotating cube to switch between full screen terms
 * Real time thumbnails of your shells
 * Special effects when closing a window
 * Various window layouts... 

%prep
%setup -q -n %{name}-0.0
sed -i 's|11 10|16 15 14 13 12 11 10|' bootstrap

%build
export LIBS=-lm
./bootstrap
%configure --disable-python
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p $RPM_BUILD_ROOT/etc/pam.d
cp -a %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/%name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_docdir}/%{name}
%{_bindir}/*
%{_mandir}/man1/%{name}.1.*
%{_sysconfdir}/pam.d/%{name}

%changelog
* Thu Jul 12 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.4342
- Rebuilt for Fedora
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.0-0.r4342.2mdv2011.0
+ Revision: 592415
- rebuild for python 2.7
* Mon Feb 08 2010 Pascal Terjan <pterjan@mandriva.org> 0.0-0.r4342.1mdv2010.1
+ Revision: 502280
- import neercs
* Tue Jan 02 2010 Pascal Terjan <pterjan@mandriva.org> 0.0-0.r4079.1mdv2010.1
- Initial package
