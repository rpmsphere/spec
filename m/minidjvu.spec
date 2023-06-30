%global __os_install_post %{nil}

Name:           minidjvu
Version:        0.8
Release:        5.1
License:        GPL-2.0
Summary:        Bitonal DjVu Encoder/Decoder
URL:            https://minidjvu.sourceforge.net/
Group:          Productivity/Graphics/Other
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE minidjvu-0.8-gzip.patch lazy.kent@opensuse.org -- gzip manpages in buildroot
Patch0:         minidjvu-0.8-gzip.patch
# PATCH-FIX-OPENSUSE minidjvu-0.8-install.patch lazy.kent@opensuse.org -- fix install options
Patch1:         minidjvu-0.8-install.patch
BuildRequires:  gcc-c++
BuildRequires:  libtiff-devel

%description
minidjvu is a command line utility which encodes and decodes single page
black-and-white DjVu files, and can compress multiple pages, taking
advantage from similarities between pages.

%package -n libminidjvu
Summary:        Bitonal DjVu Encoder/Decoder Library
Group:          System/Libraries

%description -n libminidjvu
Library for DjVu encoding/decoding black-and-white images.

%package -n libminidjvu-devel
Summary:        Minidjvu Development Files
Group:          Development/Libraries/C and C++
Requires:       libminidjvu = %{version}

%description -n libminidjvu-devel
Development files for the package minidjvu.

%prep
%setup -q
%patch0
%patch1

%build
%configure --disable-static
# Don't run parallel make because of error!
make

%install
%makeinstall
chmod 755 $RPM_BUILD_ROOT%{_libdir}/*
install -Dm 0644 %{name}.h $RPM_BUILD_ROOT%{_includedir}/%{name}.h
for x in $(find ./minidjvu -type f -name "*.h") ; do
    install -Dm 0644 ${x} $RPM_BUILD_ROOT%{_includedir}/${x}
done
rm -f $RPM_BUILD_ROOT%{_libdir}/libminidjvu.la
%find_lang %{name}

%post -n libminidjvu -p /sbin/ldconfig

%postun -n libminidjvu -p /sbin/ldconfig

%files -f %{name}.lang
%doc COPYING NEWS README
%{_bindir}/%{name}
%doc %{_mandir}/man1/*
%doc %{_mandir}/ru

%files -n libminidjvu
%{_libdir}/*.so.*

%files -n libminidjvu-devel
%doc doc/{decode.html,encode.html}
%{_libdir}/*.so
%{_includedir}/%{name}
%{_includedir}/%{name}.h

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuilt for Fedora
* Mon Feb  6 2012 lazy.kent@opensuse.org
- Corrected source URL.
* Tue Nov  8 2011 lazy.kent@opensuse.org
- Corrected License tag.
- Use full URL as a source.
- Added COPYING to docs.
- man pages marked as doc.
- spec clean up and formatting.
* Sat Jul 17 2010 lazy.kent.suse@gmail.com
- Built shared library and devel package.
* Fri Jul 16 2010 lazy.kent.suse@gmail.com
- Initial package created - 0.8.
