%global debug_package %{nil}
Summary: Lightweight video editor powered by mplayer and mencoder
Name: auteur
Version: 0.1a7
Release: 1
Source0: http://auteur-editor.info/releases/source_tarballs/%{name}-%{version}.tar.gz
License: GPL v3
Group: Application/Multimedia
BuildArch: noarch
URL: http://auteur-editor.info/
BuildRequires: python2-devel
Requires: PyQt4, mplayer, mencoder

%description
The Auteur Non-Linear Editor is a professional-grade but user-friendly video editor.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT
mv -f $RPM_BUILD_ROOT%{_bindir}/%{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/auteur

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{python2_sitelib}/%{name}-*
%{python2_sitelib}/lib_%{name}

%changelog
* Mon Feb 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1a7
- Rebuild for Fedora
* Fri Jan 28 2011 Neil Wallace <rowinggolfer@googlemail.com>
- Initial package
