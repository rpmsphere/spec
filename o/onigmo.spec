Name:           onigmo
Version:        6.2.0
Release:        1
Summary:        Regular expressions library forked from Oniguruma
License:        BSD
URL:            https://github.com/k-takata/Onigmo
Source0:        https://github.com/k-takata/Onigmo/releases/download/Onigmo-%{version}/%{name}-%{version}.tar.gz

%description
Onigmo is a regular expressions library forked from Oniguruma. It focuses to
support new expressions like \K, \R, (?(cond)yes|no) and etc. which are
supported in Perl 5.10+.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
#{__sed} -i.multilib -e 's|-L@libdir@||' onig-config.in

%build
#define _lto_cflags %{nil}
%configure \
        --enable-posix-api \
        --enable-binary-compatible-posix-api \
        --disable-silent-rules \
        --disable-static \
        --with-rubydir=%{_bindir}
%make_build

%install
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
        INSTALL="%{__install} -c -p"
find $RPM_BUILD_ROOT -name '*.la' \
        -exec %{__rm} -f {} ';'

%files
%doc    AUTHORS
%license        COPYING
%doc    HISTORY
%doc    README.md
%{_libdir}/libonigmo.so.*

%files devel
%doc    doc/API
%doc    doc/FAQ
%doc    doc/RE
%lang(ja)       %doc    doc/API.ja
%lang(ja)       %doc    doc/FAQ.ja
%lang(ja)       %doc    doc/RE.ja
%{_bindir}/onigmo-config
%{_libdir}/libonigmo.so
%{_includedir}/onig*.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 6.2.0
- Rebuilt for Fedora