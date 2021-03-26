%define __arch_install_post %{nil}

Summary:	Desktop Environment based on fvwm2
Name:		fvwm-crystal
Version:	3.4.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source:		http://download.berlios.de/fvwm-crystal/%{name}-%{version}.tar.gz
URL:		http://fvwm-crystal.berlios.de/
Requires:	ImageMagick
Requires:	aterm
Requires:	fvwm >= 2.5.13
Requires:	fvwm-perl
Requires:	habak
Requires:	mpc
Requires:	mpd
Requires:	python2
Requires:	rox
Requires:	scrot
Requires:	sudo
Requires:	trayer
#Requires:	xmms-shell
Requires:	xscreensaver
BuildArch:	noarch

%description
FVWM-Crystal is a set of configuration files for F* Virtual Window 
Manager (FVWM), which can create for you a good looking, very 
functional desktop environment.

%prep
%setup -q
#rm -rf */*/*/*/*/*/.svn */*/*/*/*/.svn */*/*/*/.svn */*/*/.svn */*/.svn */.svn .svn

%build

%install
rm -rf $RPM_BUILD_ROOT
%__make prefix=$RPM_BUILD_ROOT%_prefix install
mv %{buildroot}%{_docdir}/%{name}-%{version} %{buildroot}%{_docdir}/%{name}

#sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/fvwm-crystal/fvwm/scripts/FvwmMPD/*.py %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_docdir}/%{name}
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/man/man?/*
%{_datadir}/xsessions/%{name}.desktop

%changelog
* Wed Dec 25 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.4.1
- Rebuild for Fedora
* Tue Nov 25 2008 - john@ossii.com.tw
- Rebuild for M6(OSSII)
* Sat Sep 27 2008 - michal.smrz@opensuse.cz
- initial version for 3.0.6
