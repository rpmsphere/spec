Summary:	Cross-platform Python spreadsheet application
Name:		pyspread
Version:	2.2.3
Release:	1
License:	GPLv3
Group:		Office/Spreadsheet
URL:		https://manns.github.io/pyspread/
Source0:	https://pypi.python.org/packages/source/p/pyspread/%{name}-%{version}.tar.gz
Source1:        pyspread.xpm
BuildRequires:	python3-devel
BuildRequires:	numpy atlas
#BuildRequires:	python3-matplotlib
#BuildRequires:	python3-wxpython
#BuildRequires:	python3-gnupg
Requires:	numpy
#Requires:	python3-matplotlib-wx
#Requires:	python3-wxpython
BuildArch:  noarch

%description
Pyspread is a cross-platform Python spreadsheet application. Instead of
spreadsheet formulas, Python expressions are entered into the spreadsheet
cells. Each expression returns a Python object that can be accessed from
other cells. These objects can represent anything including lists or matrices.

%prep
%setup -q

%build
python3 setup.py build

%install
#python3 setup.py install --skip-build --root=%{buildroot} --install-lib=/usr/share/ --install-scripts=/usr/share/
python3 setup.py install --skip-build --root=%{buildroot}

install -p -m 644 -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.xpm
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.md LICENSE changelog
%{python3_sitelib}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_bindir}/%{name}
%exclude /usr/pyspread/share/applications/io.gitlab.pyspread.pyspread.desktop

%changelog
* Sun Dec 11 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.3
- Rebuilt for Fedora
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
