Name:           subst
Version:		1.0
Release:        3.1
Summary:        Subst utility from AltLinux
Group:          Console
License:        GPL
URL:            https://sisyphus.ru
Source0:        %{name}-%{version}.tar.bz2
Requires:       sed

%description
The sed-based in-place files editor, a wrapper around
sed -i --follow-symlinks.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/subst

%changelog
* Mon Feb 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
