%define ttf_fontdir %{_datadir}/fonts/roboto

Name:               roboto-fonts
Version:            2.138
Release:            1
Summary:            Android Roboto Fonts
Source:             https://github.com/google/roboto/releases/download/v%{version}/roboto-android.zip
URL:                https://github.com/google/roboto
Group:              System/X11/Fonts
License:            Apache Software License version 2.0 (ASL v2)
BuildRequires:      unzip
BuildArch:          noarch

%description
Roboto is a Helvetica alike sans serif font that was introduced with Android
4.0 (Ice Cream Sandwich).

%prep
%setup -q -c

%build

%install
%__rm -rf $RPM_BUILD_ROOT
%__install -d $RPM_BUILD_ROOT%{ttf_fontdir}
%__install -m0644 *.ttf $RPM_BUILD_ROOT%{ttf_fontdir}

%files
%license LICENSE
%{ttf_fontdir}

%changelog
* Tue Nov 26 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.138
- Rebuilt for Fedora
* Tue Nov 22 2011 pascal.bleser@opensuse.org
- initial version (1.0)
