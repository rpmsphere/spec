Name:           img2djvu
Version:        1.14
Release:        2.1
License:        Public Domain
Summary:        Single-pass DjVu Encoder Based on DjVu Libre and ImageMagick
URL:            http://github.com/ashipunov/img2djvu
Group:          Productivity/Graphics/Other
Source0:        %{name}-%{version}.tar.bz2
Requires:       ImageMagick
Requires:       djvulibre
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a single-pass DjVu encoder based on DjVu Libre and ImageMagick,
optionally also minidjvu and ocrodjvu plus Cuneiform or Tesseract.

%prep
%setup -q

%build

%install
%__rm -rf $RPM_BUILD_ROOT
install -Dm 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc NEWS README TODO
%{_bindir}/%{name}

%clean
%__rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.14
- Rebuilt for Fedora
* Tue Nov  8 2011 lazy.kent@opensuse.org
- Corrected Recommends/Suggests.
- spec clean up.
* Sun Nov 14 2010 lazy.kent.suse@gmail.com
- update to 1.14
* Sat Nov 13 2010 lazy.kent.suse@gmail.com
- update to 1.13
* Wed Nov 10 2010 lazy.kent.suse@gmail.com
- update to 1.12
* Mon Nov  8 2010 lazy.kent.suse@gmail.com
- dropped ocrodjvu_option.patch
* Fri Nov  5 2010 lazy.kent.suse@gmail.com
- update to 1.10
* Thu Nov  4 2010 lazy.kent.suse@gmail.com
- update to 1.9
* Tue Nov  2 2010 lazy.kent.suse@gmail.com
- initial package created - 1.8
