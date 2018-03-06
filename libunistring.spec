#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD605848ED7E69871 (ueno@gnu.org)
#
Name     : libunistring
Version  : 0.9.9
Release  : 13
URL      : https://mirrors.kernel.org/gnu/libunistring/libunistring-0.9.9.tar.xz
Source0  : https://mirrors.kernel.org/gnu/libunistring/libunistring-0.9.9.tar.xz
Source99 : https://mirrors.kernel.org/gnu/libunistring/libunistring-0.9.9.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: libunistring-lib
Requires: libunistring-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
GNU LIBUNISTRING - Unicode string library
This library provides functions for manipulating Unicode strings and
for manipulating C strings according to the Unicode standard.

%package dev
Summary: dev components for the libunistring package.
Group: Development
Requires: libunistring-lib
Provides: libunistring-devel

%description dev
dev components for the libunistring package.


%package dev32
Summary: dev32 components for the libunistring package.
Group: Default
Requires: libunistring-lib32
Requires: libunistring-dev

%description dev32
dev32 components for the libunistring package.


%package doc
Summary: doc components for the libunistring package.
Group: Documentation

%description doc
doc components for the libunistring package.


%package lib
Summary: lib components for the libunistring package.
Group: Libraries

%description lib
lib components for the libunistring package.


%package lib32
Summary: lib32 components for the libunistring package.
Group: Default

%description lib32
lib32 components for the libunistring package.


%prep
%setup -q -n libunistring-0.9.9
pushd ..
cp -a libunistring-0.9.9 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1520311763
%configure --disable-static
make

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 check

%install
export SOURCE_DATE_EPOCH=1520311763
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/unistring/cdefs.h
/usr/include/unistring/iconveh.h
/usr/include/unistring/inline.h
/usr/include/unistring/localcharset.h
/usr/include/unistring/stdbool.h
/usr/include/unistring/stdint.h
/usr/include/unistring/version.h
/usr/include/unistring/woe32dll.h
/usr/lib64/libunistring.so

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libunistring.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libunistring/*
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libunistring.so.2
/usr/lib64/libunistring.so.2.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libunistring.so.2
/usr/lib32/libunistring.so.2.1.0
