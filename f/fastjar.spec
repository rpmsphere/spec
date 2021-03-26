Name:         fastjar
Summary:      Fast Java Archive (JAR) Tool
URL:          http://savannah.nongnu.org/projects/fastjar
Group:        Archiver
License:      GPL
Version:      0.98
Release:      5.1
Source0:      http://download.savannah.gnu.org/releases/fastjar/fastjar-%{version}.tar.gz

%description
FastJar is an attempt at creating a feature-for-feature copy of
Sun's JDK's jar(1) command. Sun's jar(1) is written entirely in Java
which makes it very slow. Since FastJar is written in C, it can
create the same .jar file as Sun's tool in a fraction of the time.

%prep
%setup -q

%build
autoreconf -ifv

./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir}
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
#rm -f $RPM_BUILD_ROOT%{_prefix}/lib/charset.alias
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%{_bindir}/*
%{_infodir}/fastjar.info.*
%{_mandir}/man1/*.1.*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.98
- Rebuild for Fedora
