Name:		ta-lib
Summary:	Technical Analysis Library
Version:	0.4.0
Release:	7.1
License:	BSD
Group:		System/Libraries
Source:		https://sourceforge.net/projects/ta-lib/files/%{name}/%{version}/%{name}-%{version}-src.tar.gz
URL:		https://ta-lib.org/
BuildRequires:	automake libtool

%description
TA-Lib provides common functions for the technical analysis of
financial market data.

Widely used by trading software developers working with Excel,
.NET, Java, Perl, Python or C/C++.
 
* More than 150 technical analysis indicators such as ADX, MACD,
  RSI, Stochastic, Bollinger Bands etc...
* Includes candlestick pattern recognition.
* Optional abstract API allowing your code to adapt automatically
  when new functions are added!

%package devel
Summary:	Include Files and Libraries mandatory for Development
Group:		Development/Libraries/C and C++
Requires:	%{name} = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n ta-lib

%build
%configure
make CFLAGS+=-Wno-format-security

%install
%make_install
%__rm -f %{buildroot}%{_libdir}/lib*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%doc *.TXT
%{_libdir}/lib*.so.*

%files devel
%{_bindir}/ta-lib-config
%{_includedir}/ta-lib
%{_libdir}/lib*.a
%{_libdir}/lib*.so

%changelog
* Sun Jan 06 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
* Fri Sep 28 2007 Toni Graffy <toni@links2linux.de> - 0.4.0-0.pm.1
- initial version: 0.4.0
