%undefine _debugsource_packages

Name:           hinedo
Version:        0.4
Release:        1
License:        GPL
URL: 		http://rt.openfoundry.org/Foundry/Project/?Queue=814
BuildRequires:  gtk2-devel
Group:          Applications/Internet
Summary:        GTK Hinet Radio
Source0:        %{name}-%{version}.tar.bz2
Patch0:         makefile.diff
Patch1:         hinedo.c.diff
Requires:       gtk2, python, mplayer

%description
GTK Hinet Radio Tuner
Listen to the hinet radio

%prep
%setup -q
%patch0
%patch1
%{__sed} -i -e 's/Tunner/Tuner/' -e 's/的 網/的網/' %{name}.desktop
%{__sed} -i -e 's/GTK2_LIBS=/GTK2_LIBS=-lX11 -lm /' Makefile

%build
%{__make}

%install
rm -rf %{buildroot}
%{__make} DESTDIR=%{buildroot} -e LIB=lib install

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}/usr/lib/%{name}/update

%clean
rm -rf %{buildroot}

%files
%doc COPYING README
%dir /usr/lib/%{name}
/usr/lib/%{name}/update
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
* Mon Nov 19 2007 swyear <swyear@gmail.com> 0.4-11.1
- hinedo package for opensuse.
