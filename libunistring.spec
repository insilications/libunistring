#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libunistring
Version  : 0.9.10
Release  : 28
URL      : file:///insilications/build/clearlinux/packages/libunistring/libunistring-0.9.10.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/libunistring/libunistring-0.9.10.tar.gz
Summary  : Library to manipulate Unicode strings
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 GPL-3.0 LGPL-2.1
Requires: libunistring-info = %{version}-%{release}
Requires: libunistring-lib = %{version}-%{release}
BuildRequires : findutils
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : gperf
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libssl)
BuildRequires : pkgconfig(openssl)
BuildRequires : texinfo
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
GNU LIBUNISTRING - Unicode string library
This library provides functions for manipulating Unicode strings and
for manipulating C strings according to the Unicode standard.

%package dev
Summary: dev components for the libunistring package.
Group: Development
Requires: libunistring-lib = %{version}-%{release}
Provides: libunistring-devel = %{version}-%{release}
Requires: libunistring = %{version}-%{release}

%description dev
dev components for the libunistring package.


%package dev32
Summary: dev32 components for the libunistring package.
Group: Default
Requires: libunistring-lib32 = %{version}-%{release}
Requires: libunistring-dev = %{version}-%{release}

%description dev32
dev32 components for the libunistring package.


%package doc
Summary: doc components for the libunistring package.
Group: Documentation
Requires: libunistring-info = %{version}-%{release}

%description doc
doc components for the libunistring package.


%package info
Summary: info components for the libunistring package.
Group: Default

%description info
info components for the libunistring package.


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


%package staticdev
Summary: staticdev components for the libunistring package.
Group: Default
Requires: libunistring-dev = %{version}-%{release}

%description staticdev
staticdev components for the libunistring package.


%package staticdev32
Summary: staticdev32 components for the libunistring package.
Group: Default
Requires: libunistring-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the libunistring package.


%prep
%setup -q -n clone_archive
cd %{_builddir}/clone_archive
pushd ..
cp -a clone_archive build32
popd

%build
## build_prepend content
#find . -type f -name 'configure*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.ac' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.mk' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.sh' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#echo "AM_MAINTAINER_MODE([disable])" >> configure.ac
#find . -type f -name 'config.status' -exec touch {} \;
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598407596
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -fPIC $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fPIC $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common  -fno-plt
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fPIC $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fPIC $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%autogen --enable-shared --enable-static
## make_prepend content
#find . -type f -name 'Makefile*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'config.status' -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1

VERBOSE=1 V=1 make %{?_smp_mflags} check || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%autogen  --enable-shared --enable-static
## make_prepend content
#find . -type f -name 'Makefile*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'config.status' -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1

pushd ../build32/
## build_prepend content
#find . -type f -name 'configure*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.ac' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.mk' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.sh' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#echo "AM_MAINTAINER_MODE([disable])" >> configure.ac
#find . -type f -name 'config.status' -exec touch {} \;
## build_prepend end
export CFLAGS="-g -O3 -fuse-linker-plugin -pipe"
export CXXFLAGS="-g -O3 -fuse-linker-plugin -fvisibility-inlines-hidden -pipe"
export LDFLAGS="-g -O3 -fuse-linker-plugin -pipe"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen  --enable-shared --enable-static  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
## make_prepend content
#find . -type f -name 'Makefile*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'config.status' -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1598407596
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
/usr/include/unicase.h
/usr/include/uniconv.h
/usr/include/unictype.h
/usr/include/unigbrk.h
/usr/include/unilbrk.h
/usr/include/uniname.h
/usr/include/uninorm.h
/usr/include/unistdio.h
/usr/include/unistr.h
/usr/include/unistring/cdefs.h
/usr/include/unistring/iconveh.h
/usr/include/unistring/inline.h
/usr/include/unistring/localcharset.h
/usr/include/unistring/stdbool.h
/usr/include/unistring/stdint.h
/usr/include/unistring/version.h
/usr/include/unistring/woe32dll.h
/usr/include/unitypes.h
/usr/include/uniwbrk.h
/usr/include/uniwidth.h
/usr/lib64/libunistring.so
/usr/lib64/pkgconfig/libunistring.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libunistring.so
/usr/lib32/pkgconfig/32libunistring.pc
/usr/lib32/pkgconfig/libunistring.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libunistring/*

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libunistring.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libunistring.so.2
/usr/lib64/libunistring.so.2.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libunistring.so.2
/usr/lib32/libunistring.so.2.1.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libunistring.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libunistring.a
