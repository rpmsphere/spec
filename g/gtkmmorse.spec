Name: gtkmmorse
Summary: A morse code learning tool
Version: 0.9.27
Release: 7.4
License: GPL
Group: HAM Radio
Source: %{name}-%{version}.tar.bz2
BuildRequires: gtkmm24-devel gconfmm26-devel libao-devel gcc-c++
URL: http://gtkmmorse.nongnu.org/

%description
GtkMMorse is a morse code learning tool released under GPL, which provides two
type of training methods:
    * Koch method
    * Classic method
Koch is a philosophy for teaching morse based on the extensive researches of
Ludwig Koch, psychologist at Die technische Hochschule, Braunschweig, Germany,
reported in Jan-Feb. 1936.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS -std=c++11" \
./configure --prefix=/usr
make %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING INSTALL THANKS
/usr/bin/gtkmmorse
/usr/share/man/man1/gtkmmorse.1.gz

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.27
- Rebuild for Fedora
* Wed Oct 21 2009 admin@eregion.de
- initial packaging
