Name:		fotocx
Version:	25.5
Release:	1
Summary:	Editor of image files from digital cameras
License:	GPLv3
Group:		Graphics
Source0:	https://kornelix.net/downloads/downloads/fotocx-%{version}-source.tar.gz
URL:		https://kornelix.net/fotocx/fotocx.html
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	ufraw
BuildRequires:	perl-Image-ExifTool
BuildRequires:	tiff-devel
BuildRequires:	xdg-utils
BuildRequires:	imagemagick
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(champlain-0.12)
BuildRequires:  pkgconfig(libjpeg)
Requires: dcraw
Requires:	exiv2
Requires:	ufraw
Requires:	perl-Image-ExifTool
Provides: fotocx
%rename fotoxx

%description
Edit image files from a digital camera. Includes color and contrast
enhancement, red-eye removal, sharpen, crop, rotate, noise removal,
HDR (high dynamic range) and panorama image compositing, thumbnail
image browser, tag editing and search.

%prep
%autosetup -n fotocx -p1

%build
export CC=clang
export CXX=clang++
%make_build CXXFLAGS="%{optflags}" LDFLAGS="%{ldflags}" PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

# menu icon
#install -D -m 644 %{buildroot}%{_datadir}/%{name}/icons/%{name}.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
#for size in 16 24 32 48
#do
#install -d %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/
#convert -resize ${size}x${size} %{buildroot}%{_datadir}/%{name}/icons/%{name}.png %{buildroot}%{_iconsdir}/hicolor/${size}x${size}/apps/%{name}.png
#done

# (tpg) drop upstream desktop file
rm -rf %{buildroot}%{_datadir}/applications/kornelix-fotoxx.desktop

# menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Version=1.0
Name=%{name}
GenericName=Image Editor
Comment=Edit image files from a digital camera
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Graphics;X-MandrivaLinux-CrossDesktop;
EOF

%files
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/fotocx.png
%{_datadir}/metainfo/kornelix.%{name}.metainfo.xml
%{_mandir}/man1/%{name}.1*
