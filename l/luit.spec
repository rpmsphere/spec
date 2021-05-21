Name:         luit
Summary:      Transparent Locale to UTF-8 Conversion Tool
URL:          http://invisible-island.net/luit/
Group:        Charset
License:      MIT-X11
Version:      2.0
Release:      6.1
Source0:      ftp://invisible-island.net/luit/luit.tar.gz

%description
Luit is a filter that can be run between an arbitrary application
and a UTF-8 terminal emulator. It will convert application output
from the locale's encoding into UTF-8, and convert terminal input
from UTF-8 into the locale's encoding. It is mainly used to support
xterm.

%prep
%setup -q -n %{name}-20130217

%build
./configure \
    --prefix=%{_prefix}
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
