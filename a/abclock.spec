%global debug_package %{nil}

Name: abclock
Summary: Analogue Bitmap Clock
Version: 1.0d
Release: 1
Group: Amusements/Games
License: GPLv2
URL: https://www.let.rug.nl/~kleiweg/abclock/
Source0: https://www.let.rug.nl/~kleiweg/5%{name}/%{name}-%{version}.tar.gz
BuildRequires: libX11-devel

%description
Digital clocks are nice for telling exactly what time it is, but, unlike an
analogue clock, they don't give a spatial representation of time. They don't
show where time is coming from or going to.

On the other hand, a bitmap representation of a mechanical clock doesn't tell
time very accurately if the bitmap is very small. And curves and oblique lines
don't look very nice in a small, low-resolution bitmap.

So, this is something different: an analogue clock that isn't tied to the
design of the mechanical clock, but instead uses the natural properties of
bitmaps: straight lines and rectangles.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -m755 %{name} abc_img %{buildroot}%{_bindir}

%files
%doc README Changes
%{_bindir}/*

%changelog
* Wed Dec 18 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0d
- Rebuild for Fedora
