%define	_name	mffont
%define fontdir %{_datadir}/fonts/%{_name}

Summary: Open Huninn TrueType Fonts
Name: mf-fonts
Version: 2019
Release: 1
License: freeware
Group: User Interface/X
URL: https://www.mffont.com
BuildArch: noarch
Source0: %{_name}.zip
Requires: fontconfig

%description
MF fonts are freeware made by 凌景明, 凌道文.
 
%prep
%setup -q -n %{_name}

%build

%install
install -d $RPM_BUILD_ROOT%{fontdir}
install -m644 *.ttf $RPM_BUILD_ROOT%{fontdir}

%post
fc-cache 2> /dev/null

%postun
fc-cache 2> /dev/null

%files
%doc README
%{fontdir}

%changelog
* Wed Apr 15 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2019
- Initial package
