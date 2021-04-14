%global fontname cf-fanwood

Name:		%{fontname}-fonts
Summary:	Based an old-style serif typeface Fairfield
Version:	1.1
Release:	2.1
License:	MIT
Source0:	https://bitbucket.org/sortsmill/sortsmill-fonts/downloads/fanwood-1.1.zip
URL:		http://crudfactory.com/font/show/fanwood
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Requires:	fontpackages-filesystem

%description
Based on work of a famous Czech-American type designer of yesteryear.
The package includes roman and italic.

%prep
%setup -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

%files
%doc COPYING
%{_fontdir}/*.otf

%changelog
* Thu Jul 19 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
