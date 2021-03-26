Summary:	Cross-platform Python spreadsheet application
Name:		pyspread
Version:	1.1.2
Release:	4.1
License:	GPLv3
Group:		Office/Spreadsheet
URL:		http://manns.github.io/pyspread/
Source0:	https://pypi.python.org/packages/source/p/pyspread/%{name}-%{version}.tar.gz
Source1:    pyspread.xpm
BuildRequires:	python2-devel
BuildRequires:	numpy atlas
#BuildRequires:	python2-matplotlib
#BuildRequires:	python2-wxpython
#BuildRequires:	python2-gnupg
Requires:	numpy
#Requires:	python2-matplotlib-wx
#Requires:	python2-wxpython
BuildArch:  noarch

%description
Pyspread is a cross-platform Python spreadsheet application. Instead of
spreadsheet formulas, Python expressions are entered into the spreadsheet
cells. Each expression returns a Python object that can be accessed from
other cells. These objects can represent anything including lists or matrices.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --install-lib=/usr/share/ --install-scripts=/usr/share/

install -p -m 644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.xpm
rm -f %{buildroot}/%{_datadir}/README %{buildroot}/%{_datadir}/changelog
rm -f %{buildroot}/%{_datadir}/%{name}/__init__.py*
rm -f %{buildroot}/%{_datadir}/*.egg-info
mv %{buildroot}/%{_datadir}/%{name}/locale %{buildroot}/%{_datadir}/
mkdir %{buildroot}/%{_bindir}
mv %{buildroot}/%{_datadir}/%{name}/%{name} %{buildroot}/%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Pyspread
Comment=Python spreadsheet application
Exec=%{name}
Icon=%{name}
Type=Application
Categories=Office;Spreadsheet;Application;
EOF

%find_lang %{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files -f %{name}.lang
%doc README pyspread/COPYING changelog pyspread/doc/help pyspread/examples
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_bindir}/%{name}
%exclude %{_datadir}/%{name}.*
%exclude %{_datadir}/runtests.*

%changelog
* Fri Aug 10 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.2
- Rebuild for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 0.3.3-3.mga5
+ Revision: 741786
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.3.3-2.mga5
+ Revision: 687869
- Mageia 5 Mass Rebuild
  + tv <tv>
    - s/uggests:/Recommends:/
* Sun Sep 07 2014 philippem <philippem> 0.3.3-1.mga5
+ Revision: 673214
- imported package pyspread
