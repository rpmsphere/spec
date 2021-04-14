%undefine _debugsource_packages
Name:           convertall
Version:        0.8.0
Release:        1
License:        GPL-2.0+
Summary:        Graphical Unit Converter
URL:            http://convertall.bellz.org/
Group:          Productivity/Scientific/Other
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source2:        %{name}.desktop
Patch0:         python-bytecode-inconsistent-mtime_fix.patch
BuildRequires:  python3-qt4
BuildRequires:  python3
BuildArch:      noarch

%description
With ConvertAll, you can combine the units any way you want. If you want to
convert from inches per decade, that's fine. Or from meter-pounds. Or from
cubic nautical miles. The units don't have to make sense to anyone else.

%prep
%setup -q -n ConvertAll

%build

%install
rm -rf $RPM_BUILD_ROOT
python3 install.py -p %{_prefix} -d %{_datadir}/doc/packages/%{name} -i %{_datadir}/%{name}/icons -b $RPM_BUILD_ROOT
install -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Install icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,64x64,scalable}/apps
install -pm 0644 icons/convertall_sm.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -pm 0644 icons/convertall_med.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -pm 0644 icons/convertall_lg.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Remove unneeded files
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/packages/%{name}/INSTALL
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/convertall.svg
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/convertall_lg.png
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/convertall_med.png
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/convertall_sm.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%doc %dir %{_datadir}/doc/packages/%{name}
%doc %{_datadir}/doc/packages/%{name}/LICENSE
%doc %{_datadir}/doc/packages/%{name}/README.html
%{_datadir}/icons/hicolor/*/apps/%{name}*
%doc %dir %{_datadir}/doc/packages/%{name}
%doc %{_datadir}/doc/packages/%{name}/README_*.html

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.0
- Rebuilt for Fedora
* Thu Nov  3 2011 asterios.dramis@gmail.com
- Update to version 0.5.2:
  * Updates:
    + Added the microliter volume unit.
    + Added the galileo acceleration unit.
    + Added the stremma land area unit.
  * Bug Fixes:
    + Changed the method of identifying a "unitless" portion of a unit to avoid
    falsely reporting incompatibility between some units when using language
    translations.
- Spec file updates:
  * Changes based on spec-cleaner run.
  * Changed License: to GPL-2.0+.
  * Updated %%description (made it more formal).
* Wed Apr 13 2011 asterios.dramis@gmail.com
- Update to version 0.5.1b:
  * Bug Fixes:
    + Fixed inconsistencies in all three unit data translations (French, German
    and Spanish) that caused some unit conversions to fail.
* Sat Apr  2 2011 asterios.dramis@gmail.com
- Update to version 0.5.1:
  * Updates:
    + Added the link length unit.
    + Added US survey variations of the mile and chain length units.
    + Added the centigray radiation dose unit.
    + Use DOS newline characters in the Windows version of the unit data file
    for easier editing by users.
  * Bug Fixes:
    + Fixed incorrect definition of the rad radiation dose unit (it was off by
    a factor of 10).
- Spec file updates:
  * Changed License: to GPLv2+.
  * Minor other updates.
* Thu Jan 13 2011 asterios.dramis@gmail.com
- Initial release (0.5.0)
- Added a patch to fix a rpmlint warning about inconsistent mtime in python
   bytecode (convertall.pyc).
