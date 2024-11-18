Name:           wxedid
Version:        0.0.15
Release:        2.1
Summary:        Extended Display Identification Data editor
License:        GPL-3.0
Group:          Hardware/Other
URL:            https://sourceforge.net/projects/wxedid/
Source0:        https://sourceforge.net/projects/wxedid/files/wxedid-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  wxWidgets-devel

%description
wxEDID is a wxWidgets - based EDID (Extended Display Identification Data) editor.
This is an early stage of development, allowing to modify the base EDID v1.3+
structure and CEA-861 (as first extension block).
Besides normal editor functionality, the app has been equipped with a DTD
constructor, which aims to ease timings selection/editing. It's also possible to
export and import EDID data to/from text files (hex ASCII format) and also to
save the structures as a human-readable text.

%prep
%setup -q
sed -i 's:.*__DATE__.*::g' src/wxEDID_Main.cpp
sed -i 's:.*__TIME__.*::g' src/wxEDID_Main.cpp

%build
# missing whitespace
CXXFLAGS="%{optflags} " CFLAGS="%{optflags} " %configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/wxEDID

%changelog
* Mon Apr 16 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.15
- Rebuilt for Fedora
* Tue Nov 28 2017 9@cirno.systems
- update to v0.0.15
  * Fixed: (BUG) RCD_RETURN_FALSE() returns RCD_TRUE
* Mon Oct 30 2017 9@cirno.systems
- update to v0.0.14
  * Update: guilog.h v0.2
  * Fixed: Info panel: BG & FG colors were theme-dependent, which
    could make the panel look "ugly" or even completely unreadable.
    Now the FG is forced to black and the BG is white.
* Tue Sep  5 2017 9@cirno.systems
- update to v0.0.13
  * Fixed: (GCC 6.x): silenced some warnings (false-positives)
    regarding "possibly unitialized variables" in EDID_class.cpp
  * Fixed: (GCC 6.x, C11 mode): wxEDID_Main.h: C11 requires a space
    between literal and string macro [-Wliteral-suffix].
  * Update: returncode.h v0.8.3
* Sat Apr  1 2017 9@cirno.systems
- Initial commit
