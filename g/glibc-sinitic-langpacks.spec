Name:		glibc-sinitic-langpacks
Version:	2.40
Release:	99
Summary:	Locale data for some sinitic languages
License:	Public Domain
Group:		System/Internationalization
Source:		https://github.com/chinese-opendesktop/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL:		https://github.com/chinese-opendesktop/%{name}
BuildArch:	noarch
BuildRequires:  glibc-locale-source
Requires:	glibc-common
Provides:	glibc-langpack
Provides:       glibc-langpack-cmn
Provides:       glibc-langpack-nan
Provides:       glibc-langpack-hak
Provides:       glibc-langpack-lzh
Provides:       glibc-langpack-yue
Conflicts:	glibc-all-langpacks

%description
This package includes the basic information required to
support some sinitic languages in your applications.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%files
%dir /usr/lib/locale
/usr/lib/locale/*

%changelog
* Sun Dec 15 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2.40
- Rebuilt for Fedora
