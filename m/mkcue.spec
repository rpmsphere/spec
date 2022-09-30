Name:           mkcue
Version:        1
Release:        8.1
License:        LGPL-2.1
Summary:        Cue Sheets Generator
URL:            http://diplodocus.org/projects/audio/
Group:          Productivity/Multimedia/CD/Grabbers
Source:         https://diplodocus.org/dist/audio/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  automake

%description
mkcue generates cue sheets from a CD's TOC (Table Of Contents).

%prep
%setup -q
sed -i 's|byte|mybyte|' diskid.h

%build
%configure
make %{?_smp_mflags}

%install
install -Dm 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
* Tue Nov  8 2011 lazy.kent@opensuse.org
- Corrected License tag.
- Use full URL as a source.
- Added COPYING to docs.
- spec clean up.
* Sun Oct 18 2009 lazy.kent.suse@gmail.com
- spec-file corrected
- corrected License
- added Authors
* Tue Apr 28 2009 lazy.kent.suse@gmail.com
- initial package created
