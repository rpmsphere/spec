Name:           xprintidle
Version:        0.2
Release:        1
Summary:        Utility to print user's idle time in X
License:        GPL-2.0
Group:          System/X11/Utilities
Url:            http://freecode.com/projects/xprintidle
Source:         http://httpredir.debian.org/debian/pool/main/x/%{name}/%{name}_%{version}.orig.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)

%description
An utility that queries the X server for the user's idle time and
prints it to stdout (in milliseconds).

%prep
%setup -q
sed -i 's/dist-lzma //' configure.ac

%build
export LIBS="-lXext"
autoreconf -fi
%configure \
  --x-includes=%{_includedir} \
  --x-libraries=%{_libdir}
make %{?_smp_mflags}

%install
%make_install

%files
%doc COPYING NEWS README AUTHORS ChangeLog
%{_bindir}/%{name}

%changelog
* Wed Mar 29 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild

* Thu Jul  7 2016 sor.alexei@meowr.ru
- Initial package
