%global fontname ubuntu-family

Name:           %{fontname}-fonts
Version:        0.83
Release:        1
Summary:        This is the Ubuntu Font Family
License:        Ubuntu Font License 1.0
URL:            http://font.ubuntu.com/
Source0:        http://font.ubuntu.com/download/ubuntu-font-family-%{version}.zip
BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Obsoletes:      ubuntu-font-family

%description
It is a unique, custom designed font that has a very distinctive look and feel.

%prep
%setup -q -n ubuntu-font-family-%{version}
# Fix https://bugs.launchpad.net/ubuntu-font-family/+bug/744812 issue:
# Wrong font rendering for qt applications
rm Ubuntu-M.ttf Ubuntu-MI.ttf

%build
# Not build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

%_font_pkg *.ttf

%doc CONTRIBUTING.txt FONTLOG.txt README.txt TRADEMARKS.txt
%license copyright.txt LICENCE.txt LICENCE-FAQ.txt

%changelog
* Tue Nov 19 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.83
- Rebuild for Fedora
* Thu Nov 05 2015 Maxim Orlov <murmansksity@gmail.com> - 0.83-1.R
- Initial package.
