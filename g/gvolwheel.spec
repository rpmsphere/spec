Name:		gvolwheel
Version:	1.0
Release:	4.1
Summary:	Lightweight application to control the audio volume
License:	GPLv3+
Group:		Sound
Source:		http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://gvolwheel.sourceforge.net/
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	intltool

%description
GVolWheel is application which lets you control the volume easily
through a tray icon you can scroll on. Easily integrate with minimal
desktops (Openbox,IceWM,XFCE etc).

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make

%install
%__rm -rf %{buildroot}
%make_install

# remove installed doc, instead use %doc for it
%__rm -rf %{buildroot}%{_usr}/doc

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%doc COPYING ChangeLog INSTALL README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}

%changelog
* Tue Feb 17 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
* Mon May 28 2012 Andrey Bondrov <abondrov@mandriva.org> 1.0-1mdv2011.0
+ Revision: 800955
- New version 1.0, update BuildRequires
- New version: 0.7
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-2mdv2011.0
+ Revision: 611053
- rebuild
* Fri Nov 06 2009 Jérôme Brenier <incubusss@mandriva.org> 0.6-1mdv2010.1
+ Revision: 461876
- add BR : intltool
- update to new version 0.6
* Wed May 27 2009 Jérôme Brenier <incubusss@mandriva.org> 0.3-1mdv2010.0
+ Revision: 380224
- import gvolwheel