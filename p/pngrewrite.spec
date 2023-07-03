Name:         pngrewrite
Summary:      PNG Palette Reduction
URL:          https://entropymine.com/jason/pngrewrite/
Group:        Graphics
License:      Unrestricted Use
Version:      1.4.0
Release:      4.1
Source0:      https://entropymine.com/jason/pngrewrite/pngrewrite-%{version}.zip
BuildRequires: libpng-devel

%description
Pngrewrite is command-line utility that reduces the unnecessarily
large palettes that too many programs write into PNG files. It also
optimizes transparency settings, and reduces the bits-per-pixel if
possible. Handy for post-processing images before putting them on a
web site.

%prep
%setup -q -c

%build
%{__cc} %{optflags -O} \
    %{optflags} `pkg-config libpng --cflags` \
    -o pngrewrite pngrewrite.c libpngrewrite.c \
    %{optflags} `pkg-config libpng --libs`

%install
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir}
install -c -m 755 \
    pngrewrite $RPM_BUILD_ROOT%{_bindir}

%files
%{_bindir}/%{name}

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.0
- Rebuilt for Fedora
