%undefine _debugsource_packages
Name:		pypentago
Version:	0.1.0
Release:	1
Summary:	A board game pentago using Python
Summary(zh_TW):	使用 Python 的 pentago 棋盤遊戲
Group:		Amusements/Games
License:	GPL
URL:		http://sourceforge.net/projects/pypentago/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	python2-devel, python2-setuptools
Requires:	python-twisted PyQt4
BuildArch:	noarch

%description
pypentago is an open-source clone of the board game pentago.

%prep
%setup -q

%build
python2 setup.py build

%install
%__rm -rf $RPM_BUILD_ROOT
python2 setup.py install --skip-build --root $RPM_BUILD_ROOT

# .desktop
%__install -d $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Pypentago
Name[zh_TW]=Pypentago
Comment=%{Summary}
Comment[zh_TW]=使用 Python 的 pentago 棋盤遊戲
Exec=%{_bindir}/%{name}
Icon=%{python2_sitelib}/%{name}/data/icon.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}*

%post
update-desktop-database %{_datadir}/applications >/dev/null 2>&1 || :

%postun
update-desktop-database %{_datadir}/applications >/dev/null 2>&1 || :

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%{python2_sitelib}/*
%{_bindir}/pypentago
%{_bindir}/pypentagod
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Rebuilt for Fedora
* Tue Aug 17 2010 Haun-Ting Luo <kylix.lo@ossii.com.tw> 0.1.0-1
- Build rpm and source rpm
