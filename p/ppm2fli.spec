Name:           ppm2fli
Version:        2.1
Release:        3.1
Summary:        Generate FLI animation files form a series of images
Group:          Applications/Engineering
License:        GPL
URL:            http://vento.pi.tu-berlin.de/ppm2fli/main.html
Source0:        http://vento.pi.tu-berlin.de/%{name}/%{name}-%{version}.tar.gz

%description
ppm2fli generates FLI animation files form a series of images. 
unflick is a utility to extract images from a FLI animation.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS -Wl,--allow-multiple-definition"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install -m755 ppm2fli unflick $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_mandir}/man1
install -m644 ppm2fli.1 unflick.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING CHANGES
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Dec 23 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuild for Fedora
* Wed Jun 11 2014 Mathias Doreille - 2.1
- Initial package
