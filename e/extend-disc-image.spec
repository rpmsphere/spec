%undefine _debugsource_packages

Name:                   extend-disc-image
Version:                0.0.6
Summary:                Expand a VirtualBox disc image
License:                GPLv2
URL:                    https://www.davjam.org/~davjam/linux/expand-disc-image/
Group:                  Productivity/File utilities
Release:                5.1
Source:                 %{name}-%{version}.tar.gz

%description
Clones a VirtualBox disc image (VDI), expanding it by a specified number of
MBytes.

Handles both expanding or fixed images.

Creates a new UUID so both original and clone images can be managed by
VirtualBox.

%prep
%setup -n %{name}.src

%build
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m755 %{name} $RPM_BUILD_ROOT%{_bindir}

%files
%{_bindir}/%{name}
%doc README COPYING

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.6
- Rebuilt for Fedora
* Sun Nov 22 2009 David Bolt <davjam@davjam.org> 0.0.6
- Fixed another typo. Incorrectly identified static images by
-  0x00 at header offset 0x4c. Identifier is 0x02.
* Fri Nov 20 2009 David Bolt <davjam@davjam.org> 0.0.5
- More tweaks. Correctly creates new UUID.
* Fri Nov 20 2009 David bolt <davjam@davjam.org> 0.0.4
- Creates a new UUID so original and clone image can be
-  managed by VirtualBox at the same time.
* Fri Nov 20 2009 David bolt <davjam@davjam.org> 0.0.3
- More error checking
-  Won't clone a fixed image if there's insufficient space for it.
* Fri Nov 20 2009 David bolt <davjam@davjam.org> 0.0.2
- Added some additional error checking
-  Won't overwrite a file.
-  Also aborts if there's any read/write errors
* Thu Nov 19 2009 David bolt <davjam@davjam.org> 0.0.1
- First release.
- Works with fixed and expanding images
