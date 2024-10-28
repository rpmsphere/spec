%global theme_name    Equity

Name:           equity-openbox-theme
Version:        20140830
Release:        3.1
Summary:        Equity Theme for Openbox
Group:          User Interface/Desktops
License:        GPLv3
URL:            https://dysphorian.deviantart.com/art/Equity-Openbox-478991252
Source0:        equity_openbox_by_dysphorian-d7x6g0k.7z
BuildArch:      noarch      
BuildRequires:  p7zip
Requires:           openbox

%description
Needed openbox to go with equinox gtk. Didn't find anything so quickly made this
to fit.

%prep
%setup -q -c

%build

%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes
cp -pr %{theme_name} %{buildroot}%{_datadir}/themes

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Tue Dec 01 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 20140830
- Rebuilt for Fedora
