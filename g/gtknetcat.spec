Summary:	A GUI for netcat developed by LXDE project
Name:     	gtknetcat
Version:	0.1
Release:	12.1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
Requires:	netcat
BuildRequires:	gtk2-devel
BuildRequires:	intltool
BuildRequires:	glib2-devel
BuildArch:	noarch
Patch0:         gtknetcat.desktop.diff
BuildRequires:  python2

%description
Easy-to-use and handy GUI frontend of netcat (nc) command letting you
transfer files to another computer via direct wired connection.

%prep
%setup -q
%patch0

%build
export PYTHON=/usr/bin/python2
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%{find_lang} %{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name} %{buildroot}%{_libexecdir}/%{name}.py
sed -i 's|network|network-transmit|' %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%{_bindir}/%{name}
%exclude /usr/libexec
%{_datadir}/%{name}
%{python2_sitelib}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Jul 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 0.1-5mdv2011.0
+ Revision: 593900
- rebuild for py2.7
* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2010.1
+ Revision: 437830
- rebuild
* Fri Mar 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-3mdv2009.1
+ Revision: 349487
- fix netcat dependency
* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.1-2mdv2009.1
+ Revision: 325637
- rebuild
* Thu Jul 17 2008 Funda Wang <fwang@mandriva.org> 0.1-1mdv2009.0
+ Revision: 237691
- import gtknetcat
