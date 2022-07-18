Name:           cuegen
Version:        1.2.0
Release:        10.1
License:        GPL
BuildRequires:  cmake
Group:          System/Utilities
Summary:        A FLAC-compatible cuesheet generator for Linux
Source0:	http://www.cs.man.ac.uk/~slavinp/files/%{name}-%{version}.tar.bz2
Source1:	%{name}_CMakeLists.txt

%description
CUEgen is a FLAC-compatible cuesheet generator for Linux. The FLAC format allows cuesheets to be embedded in .flac files by storing 
their data in the CUESHEET metadata block. The cuesheet itself is simply a description of the contents of an audio CD. The cuesheet 
can be used in conjunction with a .flac file to store a complete album in a single FLAC file and then retrieve individual tracks fro
m that file. The cuesheet may also be used by CD burning applications to recreate an identical copy of an original audio CD from its
 FLAC representation and an associated cuesheet. As such, cuesheets are of great use in archiving, transporting and burning FLAC-enc
oded audio files.

CUEgen creates a cuesheet for any audio CD. This cuesheet may then be embedded into a FLAC file of the CD or distributed with a FLAC
 file to permit the original CD to be recreated.

CUEgen is written by Paul Slavin <slavinp@cs.man.ac.uk> and the CUEgen homepage is http://www.cs.man.ac.uk/~slavinp/cuegen.html.

CUEgen is released under the GNU General Public License, see http://www.gnu.org/copyleft/gpl.html.

%prep
%setup -q
cp %{SOURCE1} CMakeLists.txt

%build
%cmake
%cmake_build

%install
%{__rm} -rf $RPM_BUILD_ROOT
mv *-linux-build/%{name} .
%cmake_install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc README
%{_bindir}/cuegen

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora
* Sun Jul 27 2008 crrodriguez@suse.de
- fix cmake warning
* Mon Jan  7 2008 crrodriguez@suse.de
- initial version
