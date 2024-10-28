%define fontdir %{_datadir}/fonts/kosugi

Summary: Kosugi TrueType Fonts
Name: kosugi-fonts
Version: 1.01
Release: 1
License: Apache 2.0
Group: User Interface/X
URL: https://fonts.google.com/specimen/Kosugi
BuildArch: noarch
Source0: %{name}.zip
Requires: fontconfig

%description
Kosugi Maru is a Gothic Rounded design, with low stroke contrast and monospaced
metrics, and rounded terminals. A regular gothic version is available as Kosugi.
 
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
%doc *.txt
%{fontdir}

%changelog
* Tue Nov 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.01
- Initial package
