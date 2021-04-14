%undefine _debugsource_packages

Name:           tiv
Version:        1.0.0git
Release:        1
Summary:        Small C++ program to display images in a (modern) terminal
License:        Apache-2.0
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/stefanhaustein/TerminalImageViewer
Source:         TerminalImageViewer-master.zip 
BuildRequires:  ImageMagick-devel

%description
There are various similar tools (such as timg) using the unicode half block
character to display two 24bit pixels per character cell. This program
enhances the resolution by mapping 4x8 pixel cells to different unicode
characters, using the following algorithm:

For each 4x8 pixel cell of the (potentially downscaled) image:
* Find the color channel (R, G or B) that has the biggest range of values for the current cell
* Split this range in the middle and create a corresponding bitmap for the cell
* Compare the bitmap to the assumed bitmaps for various unicode block graphics characters
* Re-calculate the foreground and background colors for the chosen character

%prep
%setup -q -n TerminalImageViewer-master

%build
make -C src/main/cpp %{?_smp_mflags}

%install
install -Dm755 src/main/cpp/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Thu Nov 21 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0git
- Rebuilt for Fedora
