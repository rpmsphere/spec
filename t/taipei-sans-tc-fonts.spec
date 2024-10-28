%define fontdir %{_datadir}/fonts/taipei-sans

Summary: Taipei Sans Fonts
Name: taipei-sans-tc-fonts
Version: 1.000
Release: 0.beta
License: SIL Open Font License 1.1
Group: User Interface/X
URL: https://sites.google.com/view/jtfoundry/
BuildArch: noarch
Source0: %{name}-%{version}.beta.zip
Requires: fontconfig

%description
A neutral and simple sans typeface for Traditional Chinese
supporting nearly all Han glyphs.

%prep
%setup -q -c

%build

%install
install -d $RPM_BUILD_ROOT%{fontdir}
install -m644 *.ttf $RPM_BUILD_ROOT%{fontdir}

%post
fc-cache 2> /dev/null

%postun
fc-cache 2> /dev/null

%files
%doc LICENSE README*
%{fontdir}

%changelog
* Tue Jul 16 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.000.beta
- Initial package
