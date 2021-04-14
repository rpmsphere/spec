Summary: Standalone Player for Browser Plugins
Name: crutziplayer
Version: 0.3.0
Release: 12.1
License: GPL
Group: Application/Multimedia
URL: http://www.crutzi.info/crutziplayer
Source0: http://www.crutzi.info/sites/default/files/%{name}_%{version}_all.deb
BuildArch: noarch
BuildRequires: python2
Requires: pygtk2, flash-plugin

%description
CrutziPlayer, my own standalone player for NPAPI (and maybe Pepper)
based browser plugins (like libflashplayer.so).

%prep
%setup -T -c
ar -x %{SOURCE0}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
tar xf data.tar.gz -C $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/lib/python2.7
mv %{buildroot}%{_datadir}/pyshared %{buildroot}/usr/lib/python2.7/site-packages

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/%{name}
/usr/lib/python2.7/site-packages/%{name}
%exclude %{_datadir}/python2.7/dist-packages/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/%{name}
%{_datadir}/icons/%{name}

%changelog
* Sun May 05 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuilt for Fedora
